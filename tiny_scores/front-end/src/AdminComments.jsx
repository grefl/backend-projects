import { Form, Link, useLoaderData, useParams } from "react-router-dom";
import './styles/AdminComments.css'
export default function AdminComments() {
  const { comments } = useLoaderData();
  const {tournamentId} = useParams();
  return <div className="AdminComments">
    <div>
      <Form method="post">
        <input type='text' name="name" />
        <button type="submit">Submit</button>
      </Form>
    </div>
    <div className="AdminComments-List">
      {comments.map((comment) =>
        <Link
          key={comment.tournament_comments_id}
          to={`/admin/tournaments/${tournamentId}/comments/${comment.tournament_comments_id}/edit`}
        >
          {comment.name}
        </Link>
      )}
    </div>
  </div>;
}
