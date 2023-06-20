quote = {
  id: '123',
  id_customer: '11aa22bb',
  type: 'deck',
  date: '2023-06-14',
  deck: {
    main_areas: [{
        height: 10,
        width: 20
    }]
  },
  board_specifications: [
    {
      id_deckboard_template: 11,
      name: 'Pressure Treated Decking Boards',
      materials: [
        {
          id: 1,
          name_snapshot: 'Pressure Treated Decking Boards',
          price_snapshot: 10,
          qty: 14
        }
      ],
      tax: 6.5,
      cost: 120
    }
  ],
  profit: 5000,
  total_cost: 25300
}


deckboard_templates = [
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
    id_materials: [6,7,8,9]
  }
]

materials =  [
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

