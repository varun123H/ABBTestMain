
const express = require('express');
const connectDB = require('./config/db');
const path = require('path'); 
const app = express();

connectDB();

app.use(express.json());

app.use(express.static(path.join(__dirname, 'public')));

app.use('/products', require('./routes/productRoutes'));
app.use('/orders', require('./routes/orderRoutes'));

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
