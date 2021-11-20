from .session import s
import random
import os

api_key = os.getenv('key')


class PlayerNotFound(Exception):
	pass


class DiscordNotFound(Exception):
	pass


async def get_user_data(ign: str):
	'Returns the Discord username of a Hypixel IGN'

	async with s.get(f'https://api.slothpixel.me/api/players/{ign}') as r:
		data = await r.json()
	if not data or data.get('error'):
		raise PlayerNotFound(f'Invalid Hypixel player: {ign}')
	return data


async def get_hypixel_rank(ign: str):
	'Returns the Hypixel rank of an IGN'
	
	user_data = await get_user_data(ign)
	return user_data['rank']