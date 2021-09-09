var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        items:null,
        cur_cat:'factory',
        f_id:null,
        link_back:false,

    },
    methods:{
        get_items:function(id){
            switch(this.cur_cat){
                case 'factory':
                    axios.get('/api/collections/'+id)
                        .then(response => this.items = response.data.items);
                    this.cur_cat = 'collection';
                    this.f_id = id;
                    this.link_back = true;
                    break;
                case 'collection':
                    this.cur_cat = 'product';
                    axios.get('/api/products/'+id)
                        .then(response => this.items = response.data.items);
                    break;
            };
        },
        change_cur_cat:function(){
            switch(this.cur_cat){
                case 'collection':
                    axios.get('/api/factories')
                        .then(response => this.items = response.data.items);
                    this.link_back = false;
                    this.cur_cat = 'factory';
                    break;
                case 'product':
                    axios.get('/api/collections/'+this.f_id)
                        .then(response => this.items = response.data.items);
                    this.cur_cat = 'collection';
                    break;
            };
        },
        redirect_to_item:function(product_id){
            window.location.replace('/item/' + product_id);
        },
    },
    mounted(){
        axios.get('/api/factories')
            .then(response => this.items = response.data.items);
    },


})
