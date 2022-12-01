import { useEffect, useRef, useState } from "react";
import { useLoaderData } from "react-router-dom";
import './styles/CommentPage.css'
export default function Comment() {
  const { commentFeed } = useLoaderData();
  return <div>
    {commentFeed.map((comment) =>
      <div className="Comment">
        <p>{comment.text}</p>
        <p className="date">{comment.date_time}</p>
        <hr/>
      </div>
    )}
  </div>;
}
