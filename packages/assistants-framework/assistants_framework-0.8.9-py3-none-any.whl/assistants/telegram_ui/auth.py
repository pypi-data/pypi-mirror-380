from functools import wraps


from assistants.telegram_ui.lib import StandardUpdate
from assistants.user_data.interfaces.telegram_chat_data import NotAuthorised
from assistants.user_data.sqlite_backend.telegram_chat_data import (
    TelegramSqliteUserData,
)


chat_data = TelegramSqliteUserData()


def restricted_access(f):
    @wraps(f)
    async def wrapper(update: StandardUpdate, *args, **kwargs):
        try:
            await chat_data.check_chat_authorised(update.effective_chat.id)
        except NotAuthorised:
            if update.effective_user is None:
                raise
            await chat_data.check_user_authorised(update.effective_user.id)
        return await f(update, *args, **kwargs)

    return wrapper


def requires_superuser(f):
    @wraps(f)
    async def wrapper(*args, **kwargs):
        # Check for Update object in args (must have effective_user attribute)
        if args and hasattr(args[0], "effective_user"):
            update = args[0]
        elif len(args) > 1 and hasattr(args[1], "effective_user"):
            update = args[1]
        elif "update" in kwargs and hasattr(kwargs["update"], "effective_user"):
            update = kwargs["update"]
        else:
            raise ValueError("Update object not found in arguments")

        await chat_data.check_superuser(update.effective_user.id)

        return await f(*args, **kwargs)

    return wrapper
