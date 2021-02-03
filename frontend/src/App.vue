<template>
  <ul class="main-menu">
    <li class="logo">
      <router-link to="/" class="logo">白板</router-link>
    </li>
    <li class="home">
      <router-link to="/">Home</router-link>
    </li>
    <li class="spaces">
      <router-link to="/spaces">Spaces</router-link>
    </li>
    <li class="boards">
      <router-link to="/boards">Boards</router-link>
    </li>
  </ul>

  <router-view/>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

.main-menu {
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  flex-direction: column;
  position: fixed;
  top: 0;
  left: 0;
  border-right: 1px solid black;
  height: 100vh;

  li {
    padding: 10px;

    a:not(.logo) {
      color: #2c3e50;
      text-decoration: none;

      &.router-link-exact-active {
        color: #335ac7;
      }
    }
  }
}

@import url('https://fonts.googleapis.com/css2?family=Ma+Shan+Zheng&display=swap');
.logo {
  font-family: 'Ma Shan Zheng', cursive;
  font-size: 2rem;
  letter-spacing: -8px;
  color: black;
  text-decoration: none;
  padding: 10px;
}
</style>
