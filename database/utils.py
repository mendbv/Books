from typing import Sequence, Optional
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from .models import Book, Author, Genre


async def insert_book(
    async_session: async_sessionmaker[AsyncSession],
    obj: Book,
) -> None:
    """добавляет новую книгу в БД"""
    async with async_session() as session:
        async with session.begin():
            session.add(obj)
            await session.commit()


async def insert_author(
    async_session: async_sessionmaker[AsyncSession],
    obj: Author,
) -> None:
    """добавляет нового автора в БД"""
    async with async_session() as session:
        async with session.begin():
            session.add(obj)
            await session.commit()


async def insert_genre(
    async_session: async_sessionmaker[AsyncSession],
    obj: Genre,
) -> None:
    """добавляет новый жанр в БД"""
    async with async_session() as session:
        async with session.begin():
            session.add(obj)
            await session.commit()


async def get_all_books(
    async_session: async_sessionmaker[AsyncSession],
) -> Sequence[Book]:
    """возвращает список всех книг"""
    async with async_session() as session:
        stmt = select(Book).order_by(Book.id)
        result = await session.execute(stmt)
        return result.scalars().all()


async def get_book_by_id(
    async_session: async_sessionmaker[AsyncSession],
    book_id: int,
) -> Optional[Book]:
    """возвращает информацию о книге по ID"""
    async with async_session() as session:
        stmt = select(Book).filter(Book.id == book_id)
        result = await session.execute(stmt)
        return result.scalar_one_or_none()


async def delete_book_by_id(
    async_session: async_sessionmaker[AsyncSession],
    book_id: int,
) -> None:
    """удаляет книгу по ID"""
    async with async_session() as session:
        async with session.begin():
            stmt = select(Book).filter(Book.id == book_id)
            result = await session.execute(stmt)
            book = result.scalar_one_or_none()

            if book:
                await session.delete(book)
                await session.commit()
