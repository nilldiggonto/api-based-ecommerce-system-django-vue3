<template>
<div class="page-product">
    <div class="columns is-multiline">
        <div class="column is-9">
            <figure class="image mb-6">
                <img v-bind:src="product.get_image" alt="">
            </figure>

            <h1 class="title">{{product.name}}</h1>
            <p>{{product.description}}</p>
        </div> <!--column-->
        <div class="column is-3">
            <div class="subtitle">Information</div>
            <p><strong>Price:</strong>${{product.price}}</p>

            <div class="field has-addons mt-6">
                <div class="control">
                    <input type="number" min="1" v-model="quantity" class="input">
                </div>

                <div class="control">
                    <a href="" class="button is-dark" @click="addToCart">Add to cart</a>
                </div>
            </div>
        </div>
    </div>
</div>
    
</template>

<script>
import axios from 'axios'
export default {
    name:'Product',
    data(){
        return{
            product: {},
            quantity:1
        }
    },
    mounted() {
        this.getProduct()
    },
    methods: {

        async getProduct(){
            this.$store.commit('setIsLoading',true)
            const category_slug = this.$route.params.category_slug
            const product_slug = this.$route.params.product_slug

            await axios.get(`api/v1/products/${category_slug}/${product_slug}`)
            .then(response=>{
                this.product = response.data
                document.title = this.product.name + ' | Guitar'
            })
            .catch(error=>{
                console.log(error)
            })
            
        },
        addToCart(){
            if (isNaN(this.quantity) || this.quantity<1){
                this.quantity = 1
            }
            const item = {
                product: this.product,
                quantity: this.quantity
            }
            this.$store.commit('addToCart',item)

            toast({
                message:'Prodcut added to the cart',
                type:'is-success',
                dismissible:true,
                pauseOnHover: true,
                duration:200,
                position: 'bottom-right'
            })
        },
        
    },
}
</script>