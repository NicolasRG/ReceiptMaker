import short from 'short-uuid';

class Reciept_entry{
    
    constructor(item , price, quantity){
        this.item = item;
        this.price = price;
        this.quantity = quantity;
        this.id = short.generate();
    }

    setPrice = (price)=>{
        this.price = price
    }

    setQuantity = (quantity) => this.quantity = quantity;

    calculate = ()=>{
        return (this.quantity*this.price);
    }

}

export default Reciept_entry;