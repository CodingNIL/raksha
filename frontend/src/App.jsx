import Analyze from "./pages/Analyze";
import HowItWorks from "./pages/HowItWorks";
import Safety from "./pages/Safety";
import History from "./pages/History";
import About from "./pages/About";

function App() {
  const path = window.location.pathname;

  switch (path) {
    case "/how-it-works":
      return <HowItWorks />;

    case "/safety":
      return <Safety />;

    case "/history":
      return <History />;

    case "/about":
      return <About />;

    case "/":
    default:
      return <Analyze />;
  }
}

export default App;