<template>
    <div id="FooterTotal">
        <div id="totals_container"> 
            
            <button  v-on:click="$emit('submit-entries')"> Generate Reciept</button>
            <div> Total :  {{total}}</div>
            
        </div>
    </div>
</template>>

<script>
export default {
    name : "FooterTotal",
    components :{
    },
    props :{
        total:{
            type : Number,
            required : true
        }
    }

}
</script>

<style scoped>
    #FooterTotal {
        margin: 5px;
        color: white;
    }

    #totals_container{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

    button{
        border-radius: 10px;
        border : none;
        font-size: 15px;
        background-color: rgb(71, 71, 71);
        width : 25%;
        color: rgb(214, 214, 214);
    }

</style>