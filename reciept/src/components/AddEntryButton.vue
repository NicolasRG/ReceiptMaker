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

</style>