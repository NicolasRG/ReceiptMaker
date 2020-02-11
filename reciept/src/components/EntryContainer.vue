<template>
    <div id="Container"> 
        <EntryHeader> </EntryHeader>
        <div v-for="entry in entries" v-bind:key="entry.id"> 
            <Entry v-bind:entry="entry">
            </Entry>    
        </div>
        <EntryFooter> </EntryFooter>
    </div>
</template>>

<script>
import EntryHeader from './EntryHeader.vue';
import EntryFooter from './EntryFooter.vue';
import Entry from './Entry.vue';
//import Reciept_entry from './Data_Classes/reciept_entry.js'

export default {
    name: "EntryContainer",
    components : {
        EntryHeader,
        EntryFooter,
        Entry
    },
    props :["entries"],
    created:()=>{
        /* eslint-disable no-console */
        console.log(this);
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