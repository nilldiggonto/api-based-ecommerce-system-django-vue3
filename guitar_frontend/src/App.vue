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
        <div class="navbar-start">
          <div class="navbar-item">
            <form action="/search" method="GET">
            <div class="field has-addons">
              <div class="control">
                <input type="text" name="query" placeholder="search here" class="input">
              </div>

              <div class="control">
                <button class="button is-success">
                  <span class="icon">
                    <i class="fas fa-search"></i>
                  </span>
                </button>
              </div>
            </div>
            </form>
          </div>
        </div>
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
                 <span>cart ({{cartTotalLength}})</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading':$store.state.isLoading }">
      <div class="lds-dual-ring"></div>
    </div>

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
      cart:{
        items:[]
      }
    }
  },
  beforeCreate() {
    this.$store.commit('initializeStore')
  },
  mounted() {
    this.cart = this.$store.state.cart
  },
  computed:{
    cartTotalLength(){
      let totalLength = 0
      for (let i=0; i< this.cart.items.length; i++){
        totalLength += this.cart.items[i].quantity
      }
      return totalLength;
    }
  }
}
</script>

<style lang="scss">
// @import '../node_modules/bulma';
@import "https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css";

.lds-dual-ring{
  display: inline-block;
  width:80px;
  height: 80px;
}
.lds-dual-ring{
  content:" ";
  display:block;
  width:64px;
  height: 64px;
  margin:8px;
  border-radius: 50%;
  border: 6px solid #ccc;
  border-color: #ccc transparent #ccc transparent;
  animation: lds-dual-ring 1.2s linear infinite;
}

@keyframes lds-dual-ring{
  0%{
    transform: rotate(360deg);
  }
}

.is-loading-bar{
  height: 0;
  overflow: hidden;

  -webkit-transition: all 0.3s;
  transition: all 0.3s;

  &.is-loading{
    height: 80px;
  }
}

</style>
