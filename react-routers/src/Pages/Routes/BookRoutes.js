import { Route, Routes } from "react-router-dom";
import { BookLayout } from "../BookLayout/BookLayout";
import { Book } from "../Book";
import { NewBook } from "../NewBook";
import { BookList } from "../BookList";

export function BookRoutes() {
  return (
    <>
      <Routes>
        <Route element={<BookLayout />}>
          <Route index element={<BookList />} />
          <Route path=":id" element={<Book />} />
          <Route path="new" element={<NewBook />} />
        </Route>
      </Routes>
    </>
  );
}
