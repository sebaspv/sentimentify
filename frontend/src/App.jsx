import Header from "./components/Header";
import Hero from "./components/Hero";
import Camera from "./components/Camera";
import { Route } from "wouter";
import Footer from "./components/Footer";

const App = () => {
  return (
    <>
      <Header />
      <Route path="/">
        <Hero />
        <Camera />
      </Route>
      <Route path="/:query">
        {(params) => <h1>You search {params.query}!</h1>}
      </Route>
      <Footer />
    </>
  );
};

export default App;
