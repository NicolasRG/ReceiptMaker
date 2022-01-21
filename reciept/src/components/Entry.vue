<template>
    <div id="container">
        <div id="delete" v-on:click ="$emit('del-entry', entry.id)" >
            X
        </div>
        <div class="Field">
            <input type="text" :value="entry.item" name="item" placeholder="item" @input="onItemChange"> 
        </div>
        <div class="Field">
            <input type="number" :value="entry.quantity" name="quantity" placeholder="quantity" @input="onQuantityChange">
        </div >
        <div class="Field">
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
            this.$emit('change-item');
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
                this.$emit('change-item');
            }
    }

    }
}


</script>>

<style scoped>
    #container{
        margin-top: 5px;
        background-color: rgb(46, 104, 143);
        display: flex;
        padding-left: 10px;
        border-radius: 10px;
        padding-top : 5px;
        padding-bottom: 5px;

    }

    #delete{
        vertical-align: middle;
        width: 50px;
        margin-left: 5px;
        left:0px;
        background-color: rgb(71, 71, 71);
        color : rgb(192, 57, 57);
        padding: 1px;
        border-radius: 10px;
    }

    #delete:hover{
        background-color: white;
        color : rgb(24, 24, 24);
    }

    .Field{
        margin-left: 40px;
        width: 20%;
        text-align: center;
    }
    
    .Field input{
        border: none;
        border-bottom: rgb(70, 136, 180) solid 2px;
        background-color: rgba(255, 255, 255, 0);
        color: rgb(236, 236, 236);
        width: 95%;
        text-align: center; 

    }

    .Field input:focus{
        background-color: rgb(56, 56, 56);
    }


    ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
        color: rgb(236, 236, 236);
        opacity: .75; /* Firefox */
    }

    :-ms-input-placeholder { /* Internet Explorer 10-11 */
        color: rgb(236, 236, 236);
    }

    ::-ms-input-placeholder { /* Microsoft Edge */
        color: red;
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