from dotenv import load_dotenv
load_dotenv()

from src.core.configs import settings
from src.core.database import engine


async def create_tables() -> None:
    import src.models.__all_models
    print('Criando as tabelas no banco de dados')

    async with engine.begin() as conn:
        await conn.run_sync(settings.DBBaseModel.metadata.drop_all)
        await conn.run_sync(settings.DBBaseModel.metadata.create_all)
    print('Tabelas criadas com sucesso...')


if __name__ == '__main__':
    import asyncio

    # asyncio.run(create_tables())
    asyncio.get_event_loop().run_until_complete(create_tables())
