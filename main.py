import os
import asyncio
from database import Base, Book, Author, Genre, session, engine, utils

async def main() -> None:
    """Подключение к БД и выполнение операций"""
    # Создание таблиц
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    # экземпляр объекта Book(cmd ругался)
    book = Book(
        title="Test Book",
        author_id=10,
        genre_id=10
    )
    # передача экземпляра в функцию
    await utils.insert_book(session, obj=book)

    # вывод всей библиотеки
    books = await utils.get_all_books(session)
    for b in books:
        print(f"Book ID: {b.id}, Title: {b.title}")


if __name__ == "__main__":
    asyncio.run(main())
