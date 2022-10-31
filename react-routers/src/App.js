import "./App.css";
import { Link, Routes, Route, NavLink } from "react-router-dom";
import { Home } from "./Pages/Home";
import { NotFound } from "./Pages/NotFound";
import { Book } from "./Pages/Book";
import { BookList } from "./Pages/BookList";
import { NewBook } from "./Pages/NewBook";
import { BookLayout } from "./Pages/BookLayout/BookLayout";
import { BookRoutes } from "./Pages/Routes/BookRoutes";
import "./styles.css";

function App() {
  return (
    <>
      <Routes location="/books">
        <Route path="/books" element={<h1>Extra Content</h1>} />
      </Routes>

      <nav>
        <ul>
          <li>
            <NavLink to="/">
            
              Home
            </NavLink>
          </li>
          <li>
            <Link to="/books"> Books</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/books/*" element={<BookRoutes />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </>
  );
}

export default App;
