quote = {
  id: '123',
  customer_id: '11aa22bb',
  job_addres: 'rua arape',
  type: 'DECKING',
  date: '2023-06-14',
  profit: 5000,
  value: 25300,

  decking_info: {
    main_areas: [{
      width: 20,
      height: 10,
      height: 2
    }]
  },

  pressure_treated: [],

  structural: [],

  decking_boards: {
    selected_index: 0,
    catalog_specs: []
  },

  railling_specs: {
    selected_index: 0,
    catalog_specs: []
  },

  rain_scape_specs: [],

  finishing: {
    selected_index: 0,
    catalog_specs: []
  },

  extras: [],
}

catalog_item_spec = {
  // id_deckboard_template: 11,
  name: 'Pressure Treated Decking Boards',
  catalog_materials_specs: [],
  tax: 6.5,
  cost: 120
}

catalog_material_spec = {
  desc_snapshot: 'Pressure Treated Decking Boards',
  price_snapshot: 10,
  qty: 14
}

decking_catalog_board = [
  {
    id: 11,
    name: 'Pressure Treated Decking Boards',
    materials: [
      {
        id: 1,
        default: true
      },
      {
        id: 2,
        default: false
      },
      {
        id: 3,
        default: false
      },
      {
        id: 4,
        default: false
      },
    ]
  },
  {
    id: 12,
    name: 'Trex Select Decking',
    id_materials: [
      {
        id: 1,
        default: true
      },
      {
        id: 2,
        default: false
      }
    ]
  }
]

materials = [
  {
    id: 1,
    desc: '5/4 x 6 Pressure Treated Decking Boards (Cost by LF)',
    price: 1.5,
    supplier: 'a'
  },
  {
    id: 2,
    desc: '5/4 x 6 x 8 Pressure Treated Decking Boards',
    price: 12,
    supplier: 'a'
  },
  {
    id: 3,
    desc: '5/4 x 6 x 10 Pressure Treated Decking Boards',
    price: 15,
    supplier: 'a'
  },
  {
    id: 4,
    desc: '1 x 8 x 16 Pressure Treated Board',
    price: 32,
    supplier: 'a'
  },
  {
    id: 5,
    desc: '#9 x 2-1/2 in. Star Drive Bugle Head R4 Multi-Purpose Screw 110 counts',
    price: 12,
    supplier: 'a'
  },
]

