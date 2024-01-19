import ProjectsSideBar from "./components/ProjectsSideBar.jsx";
import NewProject from "./components/NewProject.jsx";
import NoProjectSelected from "./components/NoProjectSelected.jsx";

function App() {
  // const []

  return (
    <main className="h-screen my-8 flex gap-8">
      <ProjectsSideBar />
      <NoProjectSelected />
    </main>
  );
}

export default App;
