<script lang="ts">
  import svelteLogo from "./assets/svelte.png";
  import fastAPILogo from "./assets/fastapi.svg";

  import Counter from "./lib/Counter.svelte";
  const API_URL = "http://127.0.0.1:8000";
  let data;
  const getData = async () => {
    const response = await fetch(API_URL + "/", {
      method: "GET",
      headers: {
        "Content-type": "application/json",
      },
    });
    data = await response.json();
    data = data.info;
  };
  getData();
</script>

<main>
  <div>
    <img src={svelteLogo} alt="Svelte Logo" />
    <h1>+</h1>
    <img src={fastAPILogo} alt="FastAPI Logo" />
  </div>
  <h1>Hello {data}!</h1>

  <Counter />

  <p>
    Visit <a href="https://svelte.dev">svelte.dev</a> to learn how to build Svelte
    apps.
  </p>

  <p>
    Check out how to make APIs with <a href="https://fastapi.tiangolo.com/"
      >FastAPI</a
    > with good documentation
  </p>
</main>

<style>
  :root {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen,
      Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  }

  main {
    text-align: center;
    margin: 0 auto;
  }

  main > div {
    padding: 2rem 25rem;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  img {
    height: 16rem;
    width: 16rem;
  }

  h1 {
    color: #ff3e00;
    text-transform: uppercase;
    font-size: 4rem;
    font-weight: 100;
    line-height: 1.1;
    margin: 2rem auto;
    max-width: 14rem;
  }

  p {
    max-width: 14rem;
    margin: 1rem auto;
    line-height: 1.35;
  }

  @media (min-width: 480px) {
    h1 {
      max-width: none;
    }

    p {
      max-width: none;
    }
  }
</style>
