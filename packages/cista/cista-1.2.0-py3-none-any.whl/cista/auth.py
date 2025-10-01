import hmac
import re
from time import time
from unicodedata import normalize

import argon2
import msgspec
from html5tagger import Document
from sanic import Blueprint, html, json, redirect
from sanic.exceptions import BadRequest, Forbidden, Unauthorized

from cista import config, session
from cista.util import pwgen

_argon = argon2.PasswordHasher()
_droppyhash = re.compile(r"^([a-f0-9]{64})\$([a-f0-9]{8})$")


def _pwnorm(password):
    return normalize("NFC", password).strip().encode()


def login(username: str, password: str):
    un = _pwnorm(username)
    pw = _pwnorm(password)
    try:
        u = config.config.users[un.decode()]
    except KeyError:
        raise ValueError("Invalid username") from None
    # Verify password
    need_rehash = False
    if not u.hash:
        raise ValueError("Account disabled")
    if (m := _droppyhash.match(u.hash)) is not None:
        h, s = m.groups()
        h2 = hmac.digest(pw + s.encode() + un, b"", "sha256").hex()
        if not hmac.compare_digest(h, h2):
            raise ValueError("Invalid password")
        # Droppy hashes are weak, do a hash update
        need_rehash = True
    else:
        try:
            _argon.verify(u.hash, pw)
        except Exception:
            raise ValueError("Invalid password") from None
        if _argon.check_needs_rehash(u.hash):
            need_rehash = True
    # Login successful
    if need_rehash:
        set_password(u, password)
    now = int(time())
    u.lastSeen = now
    return u


def set_password(user: config.User, password: str):
    user.hash = _argon.hash(_pwnorm(password))


class LoginResponse(msgspec.Struct):
    user: str = ""
    privileged: bool = False
    error: str = ""


def verify(request, *, privileged=False):
    """Raise Unauthorized or Forbidden if the request is not authorized"""
    if privileged:
        if request.ctx.user:
            if request.ctx.user.privileged:
                return
            raise Forbidden("Access Forbidden: Only for privileged users", quiet=True)
    elif config.config.public or request.ctx.user:
        return
    raise Unauthorized(f"Login required for {request.path}", "cookie", quiet=True)


bp = Blueprint("auth")


@bp.get("/login")
async def login_page(request):
    doc = Document("Cista Login")
    with doc.div(id="login"):
        with doc.form(method="POST", autocomplete="on"):
            doc.h1("Login")
            doc.input(
                name="username",
                placeholder="Username",
                autocomplete="username",
                required=True,
            ).br
            doc.input(
                type="password",
                name="password",
                placeholder="Password",
                autocomplete="current-password",
                required=True,
            ).br
            doc.input(type="submit", value="Login")
        s = session.get(request)
        if s:
            name = s["username"]
            with doc.form(method="POST", action="/logout"):
                doc.input(type="submit", value=f"Logout {name}")
    flash = request.cookies.message
    if flash:
        doc.dialog(
            flash,
            id="flash",
            open=True,
            style="position: fixed; top: 0; left: 0; width: 100%; opacity: .8",
        )
    res = html(doc)
    if flash:
        res.cookies.delete_cookie("flash")
    if s is False:
        session.delete(res)
    return res


@bp.post("/login")
async def login_post(request):
    try:
        if request.headers.content_type == "application/json":
            username = request.json["username"]
            password = request.json["password"]
        else:
            username = request.form["username"][0]
            password = request.form["password"][0]
        if not username or not password:
            raise KeyError
    except KeyError:
        raise BadRequest(
            "Missing username or password",
            context={"redirect": "/login"},
        ) from None
    try:
        user = login(username, password)
    except ValueError as e:
        raise Forbidden(str(e), context={"redirect": "/login"}) from e

    if "text/html" in request.headers.accept:
        res = redirect("/")
        session.flash(res, "Logged in")
    else:
        res = json({"data": {"username": username, "privileged": user.privileged}})
    session.create(res, username)
    return res


@bp.post("/logout")
async def logout_post(request):
    s = request.ctx.session
    msg = "Logged out" if s else "Not logged in"
    if "text/html" in request.headers.accept:
        res = redirect("/login")
        res.cookies.add_cookie("flash", msg, max_age=5)
    else:
        res = json({"message": msg})
    session.delete(res)
    return res


@bp.post("/password-change")
async def change_password(request):
    try:
        if request.headers.content_type == "application/json":
            username = request.json["username"]
            pwchange = request.json["passwordChange"]
            password = request.json["password"]
        else:
            username = request.form["username"][0]
            pwchange = request.form["passwordChange"][0]
            password = request.form["password"][0]
        if not username or not password:
            raise KeyError
    except KeyError:
        raise BadRequest(
            "Missing username, passwordChange or password",
        ) from None
    try:
        user = login(username, password)
        set_password(user, pwchange)
    except ValueError as e:
        raise Forbidden(str(e), context={"redirect": "/login"}) from e

    if "text/html" in request.headers.accept:
        res = redirect("/")
        session.flash(res, "Password updated")
    else:
        res = json({"message": "Password updated"})
    session.create(res, username)
    return res


@bp.get("/users")
async def list_users(request):
    verify(request, privileged=True)
    users = []
    for name, user in config.config.users.items():
        users.append(
            {
                "username": name,
                "privileged": user.privileged,
                "lastSeen": user.lastSeen,
            }
        )
    return json({"users": users})


@bp.post("/users")
async def create_user(request):
    verify(request, privileged=True)
    try:
        if request.headers.content_type == "application/json":
            username = request.json["username"]
            password = request.json.get("password")
            privileged = request.json.get("privileged", False)
        else:
            username = request.form["username"][0]
            password = request.form.get("password", [None])[0]
            privileged = request.form.get("privileged", ["false"])[0].lower() == "true"
        if not username or not username.isidentifier():
            raise ValueError("Invalid username")
    except (KeyError, ValueError) as e:
        raise BadRequest(str(e)) from e
    if username in config.config.users:
        raise BadRequest("User already exists")
    if not password:
        password = pwgen.generate()
    changes = {"privileged": privileged}
    changes["hash"] = _argon.hash(_pwnorm(password))
    try:
        config.update_user(username, changes)
    except Exception as e:
        raise BadRequest(str(e)) from e
    return json({"message": f"User {username} created", "password": password})


@bp.put("/users/<username>")
async def update_user(request, username):
    verify(request, privileged=True)
    try:
        if request.headers.content_type == "application/json":
            changes = request.json
        else:
            changes = {}
            if "password" in request.form:
                changes["password"] = request.form["password"][0]
            if "privileged" in request.form:
                changes["privileged"] = request.form["privileged"][0].lower() == "true"
    except KeyError as e:
        raise BadRequest("Missing fields") from e
    password_response = None
    if "password" in changes:
        if changes["password"] == "":
            changes["password"] = pwgen.generate()
        password_response = changes["password"]
        changes["hash"] = _argon.hash(_pwnorm(changes["password"]))
        del changes["password"]
    if not changes:
        return json({"message": "No changes"})
    try:
        config.update_user(username, changes)
    except Exception as e:
        raise BadRequest(str(e)) from e
    response = {"message": f"User {username} updated"}
    if password_response:
        response["password"] = password_response
    return json(response)


@bp.put("/config/public")
async def update_public(request):
    verify(request, privileged=True)
    try:
        public = request.json["public"]
    except KeyError:
        raise BadRequest("Missing public field") from None
    config.update_config({"public": public})
    return json({"message": "Public setting updated"})
