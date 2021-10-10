var appp = new Vue({
    el:'#app',
    delimiters:['[[',']]'],
    data:{
        items:[],
        link_back:false,
        cur_cat:'category',
        filt:'',
        factory:'all',
        collection:'all',
        size:24,
        page_number:0,

    },
    computed:{
        pred_filtred_items:function(){
            var f = this.factory;
            var c = this.collection;
            if(f==='all'){
                if(c==='all'){
                    return this.items;
                }else{
                    return this.items.filter(function(elem){
                        return elem.collection === c;
                    });
                };
            }else{
                if(c==='all'){
                    return this.items.filter(function(elem){
                        return elem.factory === f});
                }else{
                    return this.items.filter(function(elem){
                        return elem.collection === c;
                    }).filter(function(elem){return elem.factory === f});
                };
            };
        },
        filtred_items:function(){
            this.page_number = 0;
            var f = this.filt.toLowerCase();
            return this.pred_filtred_items.filter(function(elem){
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
        factories:function(){
            var c = this.collection;
            if(c === 'all'){
                var ff = this.items.map(item => item.factory);
                var f = ff.filter((v, i, a) => a.indexOf(v) === i);
            }else{ 
                var fff = this.items.filter(function(item){
                    return item.collection === c; 
                });
                var ff = fff.map(item => item.factory);
                var f = ff.filter((v, i, a) => a.indexOf(v) === i);
            };
            return f.sort()
        },
        collections:function(){
            var f = this.factory;
            if(f === 'all'){
                var cc = this.items.map(item => item.collection);
                var c = cc.filter((v, i, a) => a.indexOf(v) === i);
            }else{
                var ccc = this.items.filter(function(item){
                    return item.factory === f; 
                });
                var cc = ccc.map(item => item.collection);
                var c = cc.filter((v, i, a) => a.indexOf(v) === i);
            }
            return c.sort();

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
            this.items=[];
            this.cur_cat = 'category';
            this.link_back = false;
            this.filt = '';
            this.page_number = 0;
            this.factory = 'all';
            this.collection = 'all';
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
