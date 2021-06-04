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

  <ProductBox
  v-for="product in latestProducts"
  v-bind:key="product.id"
  v-bind:product = "product"
  />
  <!-- --column-3---> -->
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import ProductBox from '@/components/ProductBox'
import axios from 'axios'
export default {
  name: 'Home',
  data(){
    return {
      latestProducts: []
    }
  },
  components:{
    ProductBox

  },
  mounted() {
    this.getLatestProducts()
    document.title ='Home | Guitar'

  },
  methods: {
    async getLatestProducts(){
      this.$store.commit('setIsLoading',true)
      await axios
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

