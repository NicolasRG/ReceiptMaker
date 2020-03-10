<template>
    <div id="Container"> 
        <EntryHeader> </EntryHeader>
        <div v-for="entry in entries" v-bind:key="entry.id"> 
            <Entry v-bind:entry = "entry"
                v-on:change-price="$emit('change-price')"
                v-on:del-entry="$emit('del-entry', entry.id)"> 
            </Entry>    
        </div>
        <AddEntryButton v-on:add-entry="$emit('add-entry')"></AddEntryButton>
        <EntryFooter> </EntryFooter>
    </div>
</template>>

<script>
import EntryHeader from './EntryHeader.vue';
import EntryFooter from './EntryFooter.vue';
import Entry from './Entry.vue';
import AddEntryButton from './AddEntryButton.vue';
//import Reciept_entry from './Data_Classes/reciept_entry.js'

export default {
    name: "EntryContainer",
    components : {
        EntryHeader,
        EntryFooter,
        Entry,
        AddEntryButton
    },
    props : {
        entries:{
            type : Array,
            required : true,
        }
    },
    created(){
        /* eslint-disable no-console */
       console.log(this);
        
    },
    methods:{
        testClick(){
            /* eslint-disable no-console */
            console.log(this);
        }
    }
    
}
</script>>

<style scoped>

#Container{
    position: relative;
    background-color: grey;
    flex-grow: auto;
    margin:10px;
    height: 100%;
}



</style>