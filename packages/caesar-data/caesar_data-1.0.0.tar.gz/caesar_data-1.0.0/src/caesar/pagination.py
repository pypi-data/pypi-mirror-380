# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from ._models import BaseModel
from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["PaginationPagination", "SyncPagination", "AsyncPagination"]

_T = TypeVar("_T")


class PaginationPagination(BaseModel):
    has_next: Optional[bool] = None

    page: Optional[int] = None


class SyncPagination(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_next = None
        if self.pagination is not None:
            if self.pagination.has_next is not None:
                has_next = self.pagination.has_next
        if has_next is not None and has_next is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.pagination is not None:
            if self.pagination.page is not None:
                current_page = self.pagination.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})


class AsyncPagination(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    data: List[_T]
    pagination: Optional[PaginationPagination] = None

    @override
    def _get_page_items(self) -> List[_T]:
        data = self.data
        if not data:
            return []
        return data

    @override
    def has_next_page(self) -> bool:
        has_next = None
        if self.pagination is not None:
            if self.pagination.has_next is not None:
                has_next = self.pagination.has_next
        if has_next is not None and has_next is False:
            return False

        return super().has_next_page()

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        current_page = None
        if self.pagination is not None:
            if self.pagination.page is not None:
                current_page = self.pagination.page
        if current_page is None:
            current_page = 1

        return PageInfo(params={"page": current_page + 1})
