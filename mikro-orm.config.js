const { MySqlDriver } = require('@mikro-orm/mysql');
require('dotenv').config();

module.exports = {
  driver: MySqlDriver,
  dbName: process.env.DB_NAME || 'api_database',
  user: process.env.DB_USER || 'root',
  password: process.env.DB_PWD || '',
  host: process.env.DB_HOST || 'localhost',
  port: parseInt(process.env.DB_PORT, 10) || 3306,
  entities: ['./src/entities/**/*.ts'],
  entitiesTs: ['./src/entities/**/*.ts'],
  debug: true
};
