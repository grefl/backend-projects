import { Form, Link, useLoaderData, useParams } from "react-router-dom";
import './styles/AdminComments.css'

export default function AdminCommentFeedEditor() {
  const { commentFeed } = useLoaderData();
  const {tournamentId, tournamentCommentsId} = useParams();
  return <div className="AdminComments">
    <section className="AdminFeedEditor">
      <Form method="post">
        <input type='text' name="text" />
        <button type="submit">Submit</button>
      </Form>
    </section>
    <section className="AdminComments-List">
      {commentFeed.map((comment) =>
        <p
          key={comment.comment_id}
        >
          {comment.text}
        </p>
      )}
    </section>
  </div>;
}