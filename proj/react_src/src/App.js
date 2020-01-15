import React from 'react';
import logo from './logo.svg';
// import './App.css';

import ReactDOM from 'react-dom';
import 'antd/dist/antd.css';
import './index.css';
import { Table } from 'antd';
import reqwest from 'reqwest';


function onChange(pagination, filters, sorter, extra) {
  console.log('params', pagination, filters, sorter, extra);
}

const columns = [
  {
    title: 'id',
    dataIndex: 'id',
    sorter: true,
    width: '20%',
    sorter: (a, b) => a.id - b.id,
    sortDirections: ['descend'],
  
  },
  {
    title: 'inventory_number',
    dataIndex: 'inventory_number',
    sorter: (a, b) => a.inventory_number - b.inventory_number,
    
    width: '20%',
    filters: [
      {
        text: '26076',
        value: '26076',
      },
      {
        text: 'Jim',
        value: 'Jim',
      },
      {
        text: 'Submenu',
        value: 'Submenu',
        children: [
          {
            text: 'Green',
            value: 'Green',
          },
          {
            text: 'Black',
            value: 'Black',
          },
        ],
      },
    ],
    // specify the condition of filtering result
    // here is that finding the name started with `value`
    onFilter: (value, record) => record.inventory_number.indexOf(value) === 0,
  },
  {
    title: 'person_id',
    dataIndex: 'person_id',
  },
];

class App extends React.Component {
  state = {
    data: [],
    pagination: {},
    loading: false,
  };

  componentDidMount() {
    this.fetch();
  }

  handleTableChange = (pagination, filters, sorter) => {
    const pager = { ...this.state.pagination };
    pager.current = pagination.current;
    this.setState({
      pagination: pager,
    });
    this.fetch({
      results: pagination.pageSize,
      page: pagination.current,
      sortField: sorter.field,
      sortOrder: sorter.order,
      ...filters,
    });
  };

  fetch = (params = {}) => {
    console.log('params:', params);
    this.setState({ loading: true });
    reqwest({
      url: 'http://127.0.0.1:8000/api/v1/inventory/device/',
      method: 'get',
      data: {
        ...params,
      },
      type: 'json',
    }).then(data => {
      const pagination = { ...this.state.pagination };
      // Read total count from server
      pagination.total = data.totalCount;
      // pagination.total = 200;
      this.setState({
        loading: false,
        data: data,
        pagination,
      });
    });
  };

  

  render() {
    return (
      <Table
        columns={columns}
        rowKey={record => record.id}
        dataSource={this.state.data}
        pagination={this.state.pagination}
        loading={this.state.loading}
        onChange={this.handleTableChange}
        
      />
    );
  }
}

          


export default App;
