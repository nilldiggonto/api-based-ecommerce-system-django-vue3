<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-brand">
        <router-link to="/" class="navbar-item"> <strong>Guitar</strong> </router-link>

        <a aria-label="menu" aria-expanded="false" data-target="navbar-menu" class="navbar-burger" @click="showMobileMenu = !showMobileMenu">
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>

        </a>
      </div> <!--navbar brand-->

      <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
        <div class="navbar-end">
          <router-link to="/rock" class="navbar-item" >Rock</router-link>
          <router-link to="/bass" class="navbar-item">Bass</router-link>

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/log-in" class="button is-light">Log in</router-link>

              <router-link to="/cart" class="button is-success">
                <span class="icon">
                  <i class="fas fa-shopping-cart"></i>
                </span>
                 <span>cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <!--navbar ended -->
  <div class="section">
    <router-view/>
  </div>

  <footer class="footer">
    <p class="has-text-centered">
      Copyright (c) 2021
    </p>
  </footer>

    <!-- <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> -->
  </div>
</template>

<script>
export default {
  data(){
    return{
      showMobileMenu:false,
    }
  }
}
</script>

<style lang="scss">
// @import '../node_modules/bulma';
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css";
</style>
