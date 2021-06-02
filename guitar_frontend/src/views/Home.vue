<template>
  <div class="home">
  <!-- <h4>Home</h4> -->
  <section class="hero is-medium is-dark mb-6">
    <div class="hero-body has-text text-centered">
      <p class="title mb-6">
        GUITAR SHOP
      </p>
      <p class="subtitle">
        Guitar store online
      </p>
    </div><!--hero body-->
  </section>

  <div class="columns is-multiline">
    <div class="column is-12">
      <h2 class="is-size-2 has-text-centered">
        Latest Product
      </h2>
    </div><!--column-->
    <!-- <p>{{latestProducts}}</p> -->

    <div class="column is-3" v-for="product in latestProducts" v-bind:key="product.id">
      <div class="box">
        <figure class="image mb-4">
          <img v-bind:src="product.get_thumbnail" alt="">
        </figure>
        <h3 class="is-size-4">
          {{product.name}}
        </h3>
        <p class="is-size-6 has-text-grey">
          ${{product.price}}

          <router-link v-bind:to="product.get_absolute_url" class="button is-dark mt-4">View Details</router-link>
        </p>
      </div>
    </div><!--column-3--->
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      latestProducts: []
    }
  },
  components:{

  },
  mounted() {
    this.getLatestProducts()
  },
  methods: {
    getLatestProducts(){
      axios
        .get('api/v1/latest-products/')
        .then(response => {
          console.log(response.data)
          this.latestProducts = response.data
        })
        .catch(error=>{
          console.log(error)
        })
    }
  },
}
</script>

<style scoped>
  .image{
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
