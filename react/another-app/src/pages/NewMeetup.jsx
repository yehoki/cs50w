import { useNavigate } from "react-router-dom";

import NewMeetupForm from "../components/meetups/NewMeetupForm";

function NewMeetupPage() {
  const navigate = useNavigate();
  function addMeetupHandler(meetupData) {
    fetch(
      "https://react-getting-started-21396-default-rtdb.firebaseio.com/meetups.json",
      {
        method: "POST",
        body: JSON.stringify(meetupData),
        header: {
          "Content-Type": "application/json",
        },
      }
    ).then(() => {
      navigate('/', {replace: true});
    });
  }

  return (
    <section>
      <NewMeetupForm onAddMeetup={addMeetupHandler} />
      <h1>Add a new meetup</h1>
    </section>
  );
}
export default NewMeetupPage;
