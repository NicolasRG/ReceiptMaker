<template>
  <div id="app">
    <Header> </Header>
    <EntryContainer :entries = "this.entries" 
      v-on:del-entry = "this.deleteEntry" 
      v-on:add-entry = "this.addEntry"
      v-on:change-price = "this.onEntryPriceChange"
      v-on:change-item = "this.onEntryItemChange"
      v-on:change-quantity = "this.onEntryQuantityChange"
     
    > </EntryContainer>
    <Footer  v-on:submit-entries = "this.submitEntries" 
        :total = "this.total"> </Footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import EntryContainer from './components/EntryContainer.vue';
import Footer from './components/Footer';
import Reciept_entry  from './components/Data_Classes/reciept_entry.js';
import axios from 'axios';
import printJS  from 'print-js';

export default {
  name: 'app',
  components: {
    Header,
    EntryContainer,
    Footer},
  data() {
    return {
      entries : [],
      total : 0,
    }
  },
  methods:{

    addEntry(name, price , quantity){
      this.entries.push(new Reciept_entry(name, price,quantity));
    },
    deleteEntry(id){
      this.entries = this.entries.filter( entry => entry.id !== id);
    },
    onEntryItemChange(){
      /*
      let entry = this.entries.find((ele)=>{
        return ele.id == id ;
      });
      entry.item = item;*/
      
      /* eslint-disable no-console */
      let price = 0;
      console.log("changed price total")
      console.log(typeof this.entries)

      this.entries.forEach(element => {
        price = price + (element.quantity*element.price);      
      });
      this.total = price;

    },
    onEntryPriceChange(id, price){
      
      let entry = this.entries.find((ele)=>{
        return ele.id == id ;
      });
      entry.price = price;

    },
    onEntryQuantityChange(id, quantity){
      
      let entry = this.entries.find((ele)=>{
        return ele.id == id ;
      });
      entry.quantity = quantity;
    
    },
    submitEntries(){
      /* eslint-disable no-console */
      const json_items = JSON.stringify(this.entries);
      console.log(json_items);
      alert(this.total);
      axios({
        method: 'post',
        url: 'http://localhost/spawnPython',
        headers: {'Content-Type': 'application/json'},
        data: {"items": json_items} 
      }).then(res =>{
        console.log(res);
        //created way to print the pdf
        var file = new Blob([res.data], {type: 'application/pdf'});
        var fileURL = URL.createObjectURL(file);
        printJS(fileURL);
        //window.open(fileURL);
      });
    },

  },
   created(){
     /* eslint-disable no-console */
    }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  display: flex;
  flex-direction: column;
  position: absolute;
  width: 100%;
  height: 100%;
}

</style>
