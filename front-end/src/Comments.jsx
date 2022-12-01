import { Link, useLoaderData } from "react-router-dom";
export default function Comments() {
  const { comments } = useLoaderData();

  return <div>
    {comments.map((comment) =>
      <Link to={`${comment.tournament_comments_id}`}>{comment.name}</Link>
    )}
  </div>;
}
