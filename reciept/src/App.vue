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
    <Footer> </Footer>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import EntryContainer from './components/EntryContainer.vue';
import Footer from './components/Footer';
import Reciept_entry  from './components/Data_Classes/reciept_entry.js';

export default {
  name: 'app',
  components: {
    Header,
    EntryContainer,
    Footer},
  data() {
    return {
      entries : [] 
    }
  },
  methods:{

    addEntry(name, price , quantity){
      this.entries.push(new Reciept_entry(name, price,quantity));
    },
    deleteEntry(id){
      this.entries = this.entries.filter( entry => entry.id !== id);
    },
    onEntryItemChange(id, item){
      
      let entry = this.entries.find((ele)=>{
        return ele.id == id ;
      });
      entry.item = item;

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
    /*getPrices(){
      
    },*/

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
