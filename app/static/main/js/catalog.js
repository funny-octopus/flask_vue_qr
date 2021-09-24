var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        items:[],
        link_back:false,
        cur_cat:'category',
        filt:'',
        size:24,
        page_number:0,

    },
    computed:{
        filtred_items:function(){
            this.page_number = 0;
            var f = this.filt.toLowerCase();
            return this.items.filter(function(elem){
                if(f==='')return true;
                else return elem.name.toLowerCase().indexOf(f) > -1 || elem.article.toLowerCase().indexOf(f) > -1;
            });
        },
        page_count:function(){
            var l = this.filtred_items.length,
                s = this.size;
            return Math.ceil(l/s);
        },
        paginated_data:function(){
            const start = this.page_number * this.size,
                  end = start + this.size;
            return this.filtred_items.slice(start, end);
        },

    },
    methods:{
        get_items:function(id){
            this.items=[];
            this.cur_cat = 'product';
            this.link_back = true;
            this.page_number = 0;
            axios.get('/api/products/'+id)
                    .then(response => this.items = response.data.items);
        },
        change_cur_cat:function(){
            this.cur_cat = 'category';
            this.link_back = false;
            this.filt = '';
            this.page_number = 0;
            axios.get('/api/category/')
                .then(response => this.items = response.data.items);
        },
        redirect_to_item:function(product_id){
            window.location.replace('/item/' + product_id);
        },
        next_page:function(){
            this.page_number++;
        },
        prev_page:function(){
            this.page_number--;
        },
    },
    beforeCreate(){
        axios.get('/api/category/')
            .then(response => this.items = response.data.items);
    },


})
