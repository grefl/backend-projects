import { redirect } from "react-router-dom";

export const BASE_URL = "http://localhost:5000/api";

export async function commentPageLoader({ params }) {
  const response = await fetch(
    `${BASE_URL}/tournaments/${params.tournamentId}/comments`,
  );

  const comments = await response.json();

  return { comments };
}

export async function commentLoader({ params }) {
  const response = await fetch(
    `${BASE_URL}/tournaments/${params.tournamentId}/comments/${params.tournamentCommentId}`,
  );

  const commentFeed = await response.json();

  return { commentFeed };

}

export const adminCommentsLoader = commentPageLoader;

async function addTournamentComment(tournamentId, formData) {
  console.log(formData)
  const result = await fetch(`${BASE_URL}/tournaments/${tournamentId}/comments/add`, {
    method: 'post',
    body: formData,
  });
  return result

}

async function addTournamentFeedComment(tournamentId, tournamentCommentId,formData) {
  console.log(formData)
  const result = await fetch(`${BASE_URL}/tournaments/${tournamentId}/comments/${tournamentCommentId}/add`, {
    method: 'post',
    body: formData,
  });
  return result

}
export async function createComment({ request, params }) {
  const formData = await request.formData();

  const result = await addTournamentComment(params.tournamentId, formData)
  console.log({ result });

  redirect(`/admin/tournaments/${params.tournamentId}/comments`)
}
export async function adminCommentFeedEditorLoader({ params }) {
  const response = await fetch(
    `${BASE_URL}/tournaments/${params.tournamentId}/comments/${params.tournamentCommentsId}`,
  );

  const commentFeed = await response.json();
  console.log({commentFeed})

  return { commentFeed }
}
export async function adminCommentFeedEditorAction({ request, params }) {
  const formData = await request.formData();

  const result = await addTournamentFeedComment(params.tournamentId,params.tournamentCommentsId, formData)
  console.log({ result });

  redirect(`/admin/tournaments/${params.tournamentId}/comments/${params.tournamentCommentsId}/edit`)
}