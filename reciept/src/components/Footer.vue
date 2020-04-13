<template>
    <div id="Footer"> 
        <footer-total v-on:submit-entries ="$emit('submit-entries')"
        :total = "total"> </footer-total>
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
        }
    },
}
</script>>

<style scoped>
    #Footer{
        flex: none;
        padding-left: 10px;
        padding-right: 10px;
    }
</style>