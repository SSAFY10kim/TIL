import { useState, useEffect } from 'react';

import { useParams } from 'react-router-dom';

export default function EventDetailPage() {
  const params = useParams();

  return (
    <>
      <h1>EventDetailPage</h1>
      <p>Event ID: {params.eventId}</p>
    </>
  );
}
