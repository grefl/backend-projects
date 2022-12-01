import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";
import { adminCommentFeedEditorAction,adminCommentFeedEditorLoader, adminCommentsLoader, commentLoader, commentPageLoader, createComment } from "./api";
import Comment from "./Comment";
import Comments from "./Comments";
import AdminComments from "./AdminComments";
import AdminCommentFeedEditor from "./AdminCommentFeedEditor";
import { createBrowserRouter, Route, RouterProvider } from "react-router-dom";
import "./index.css";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
  },
  {
    path: "/tournaments/:tournamentId/comments",
    element: <Comments />,
    loader: commentPageLoader,
  },
  {
    path: "/tournaments/:tournamentId/comments/:tournamentCommentId",
    element: <Comment />,
    loader: commentLoader,
  },
  {
    path: "/admin/tournaments/:tournamentId/comments",
    element: <AdminComments />,
    loader: adminCommentsLoader,
    action: createComment
  },
  {
    path: "/admin/tournaments/:tournamentId/comments/:tournamentCommentsId/edit",
    element: <AdminCommentFeedEditor />,
    loader: adminCommentFeedEditorLoader,
    action: adminCommentFeedEditorAction
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
);
