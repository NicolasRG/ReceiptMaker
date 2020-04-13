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
        background-color: black;
        color: white;
    }

    #totals_container{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

</style>