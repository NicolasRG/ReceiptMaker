<template>
    <div id="Container"> 
        <EntryHeader> </EntryHeader>
        <div v-for="entry in entries" v-bind:key="entry.id"> 
            <Entry v-bind:entry = "entry"
                v-on:change-price="$emit('change-price')"
                v-on:del-entry="$emit('del-entry', entry.id)"
                v-on:change-item="$emit('change-item')"> 
            </Entry>    
        </div>
        <EntryFooter v-on:add-entry="$emit('add-entry')"> 
        </EntryFooter>
    </div>
</template>>

<script>
import EntryHeader from './EntryHeader.vue';
import EntryFooter from './EntryFooter.vue';
import Entry from './Entry.vue';

export default {
    name: "EntryContainer",
    components : {
        EntryHeader,
        EntryFooter,
        Entry,
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
    background-color: rgb(60, 139, 192);
    border: rgb(24, 81, 122) 2px solid ;
    flex-grow: auto;
    margin:10px;
    margin-bottom: 0px;
    height: 100%;
    border-radius: 5px;
}



</style>