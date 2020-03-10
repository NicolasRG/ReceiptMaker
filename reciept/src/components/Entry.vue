<template>
    <div id="container">
        <div id="delete" v-on:click ="$emit('del-entry', entry.id)">
            X
        </div>
        <div>
            <input type="text" :value="entry.item" name="item" placeholder="item" @input="onItemChange"> 
        </div>
        <div>
            <input type="number" :value="entry.quantity" name="quantity" placeholder="quantity" @input="onQuantityChange">
        </div>
        <div>
            <input type="number" step="any" :value="entry.price"  name="price" placeholder="price per" @input="onPriceChange">
        </div>
    </div>
</template>

<script>
export default {
    data(){
        return{
            item: '',
            quantity : 0,
            price : 0,
        }
    },
    props:{
        entry: Object,
    },
    created: ()=>{
        /* eslint-disable no-console */
        //console.log(this.entry);
    },
    methods:{
        onItemChange(e){
            console.log(e.target.value);
            this.entry.setItem(e.target.value);
        },
        onQuantityChange(e){
            console.log(e.target.value);
            this.entry.setQuantity(e.target.value);
        },
        onPriceChange(e){
            const price = e.target.value;
            console.log(price);
            const decimal = price.split(".")[1];
            if(decimal != undefined ){
                if(decimal.length <= 2){
                this.entry.setPrice(e.target.value);
                this.price = e.target.value;
                }
                else{
                    this.price = this.entry.price;
                    e.preventDefault();
                    console.log("prevent defualt");
                    return false}            
            }else{
                
                this.entry.setPrice(e.target.value);
                this.price = e.target.value;
            }
    }

    }
}


</script>>

<style scoped>
    #container{
        background-color: burlywood;
        border: black 1px solid;
        display: flex;
        justify-content: space-around;
    }

    #delete{
        max-width: 100px;
        left:0px;
    }

    /* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance:textfield;
}

</style>