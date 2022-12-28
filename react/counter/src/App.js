import Todo from "./components/Todo";
import "./modules/App.css";

function App() {
  return (
    <div>
      <h1>Todo</h1>
      <Todo text = "1234"/>
      <Todo text = "Testing"/>
      <Todo text = "hehe"/>
      <Todo text = "Another one let's go champ"/>
    </div>
  );
}
export default App;
