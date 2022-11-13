from  create_bot import dp
from aiogram.utils import executor

from handlers import  client,admin,other

client.register_handlers_client(dp)
#other.register_handlers_client(dp)


executor.start_polling(dp, skip_updates=True)

