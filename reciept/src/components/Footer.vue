<template>
    <div id="Footer"> 
        <footer-total v-on:submit-entries ="$emit('submit-entries')"
        :total = "total"> </footer-total>
        <div>
            Tax = {{tax}}
        </div>
    </div>
</template>

<script>
import FooterTotal from './FooterTotal.vue';
export default {
    name : "Footer",
    components : {
        FooterTotal
    },
    props : {
        total:{
            type : Number,
            required : true,
        },
        tax:{
            type : Number,
            required : true,
        }
    },
}
</script>>

<style scoped>
    #Footer{
        flex: none;
        padding: 5px;
        border-radius: 10px;
        margin-bottom: 40px;
        margin-top : 10px;
        margin-left: 10px;
        margin-right: 10px;
        background-color: rgb(60, 139, 192);
    }
</style>