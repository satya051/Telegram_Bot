async def is_admin(update) -> bool:
    chat_id = update.effective_chat.id
    user_id = update.effective_user.id
    admins = await update.effective_chat.get_administrators()
    return any(admin.user.id == user_id for admin in admins)
