<template>
    <div class="page-category">
        <div class="columns is-multiline">
            <div class="column is-12">
                <h2 class="is-size-2 has-text-centered">
                    {{category.name}}
                </h2>
            </div>

            <!--category-->
          <ProductBox
            v-for="product in category.products"
            v-bind:key="product.id"
            v-bind:product = "product"
            />

        </div>
    </div>
</template>

<script>
import ProductBox from '@/components/ProductBox'

import axios from 'axios'
import { toast } from 'bulma-toast'
export default {
    name: 'Category',
     components:{
            ProductBox

  },
    data(){
        return {
            category:{
                products : []
            }
        }
    },
    mounted() {
        this.getCategory()
    },
    watch:{
        $route(to,from){
            if (to.name === 'Category'){
                this.getCategory()
            }
        }
    },
    methods: {
        async getCategory(){
            const categorySlug = this.$route.params.category_slug
            
            this.$store.commit('setIsLoading',true)

            axios.get(`/api/v1/products/${categorySlug}/`)
            .then(response =>{
                this.category = response.data
                document.title = this.category.name + ' | Guitars'
            })
            .catch(error => {
                console.log(error)
                toast({
                    message:'something not right',
                    type: 'is-danger',
                    dismissible: true,
                    pauseOnHover: true,
                    duration: 2000,
                    position: 'bottom-right',
                })
            })
        }
    },
}
</script>