<template>
    <div id="container">
        <button v-on:click="this.addEntry"> Add entry</button>
    </div>
</template>

<script>
import Reciept_entry from './Data_Classes/reciept_entry.js';
export default {
    name :"AddEntryButton",
    methods:{
        addEntry(){
            const entry = new Reciept_entry('item', '1', '2.00');//need to change at some point
            this.$emit('add-entry',entry);
        }
    }
}
</script>

<style scoped>
    button{
        border-radius: 10px;
        border : none;
        font-size: 15px;
        background-color: rgb(71, 71, 71);
        width : 33%;
        color: rgb(214, 214, 214);
    }

    button:hover{
        background-color: rgb(15, 64, 97);
        color: white;
    }


</style>