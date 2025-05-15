require 'date'

class ElectricityReadingsGenerator
  def generate(number)
    now = DateTime.now
    one_second = Rational(1, 24 * 60 * 60)
    
    (0..number-1).map do |n|
      {
        'time' => (now - n * one_second).to_s,
        'reading' => rand(0.5..1.5)
      }
    end
  end
end





DR_EVILS_DARK_ENERGY_ENERGY_SUPPLIER = "Dr Evil's Dark Energy";
THE_GREEN_ECO_ENERGY_SUPPLIER = "The Green Eco";
POWER_FOR_EVERYONE_ENERGY_SUPPLIER = "Power for Everyone";

MOST_EVIL_PRICE_PLAN_ID = "price-plan-0";
RENEWABLES_PRICE_PLAN_ID = "price-plan-1";
STANDARD_PRICE_PLAN_ID = "price-plan-2";

SARAHS_SMART_METER_ID = "smart-meter-0";
PETERS_SMART_METER_ID = "smart-meter-1";
CHARLIES_SMART_METER_ID = "smart-meter-2";
ANDREAS_SMART_METER_ID = "smart-meter-3";
ALEXS_SMART_METER_ID = "smart-meter-4";

def smart_meter_to_price_plan_accounts
  {
    SARAHS_SMARTa_METER_ID => MOST_EVIL_PRICE_PLAN_ID,
    PETERS_SMART_METER_ID => RENEWABLES_PRICE_PLAN_ID,
    CHARLIES_SMART_METER_ID => MOST_EVIL_PRICE_PLAN_ID,
    ANDREAS_SMART_METER_ID => STANDARD_PRICE_PLAN_ID,
    ALEXS_SMART_METER_ID => RENEWABLES_PRICE_PLAN_ID
  }
end

def readings
  reading_generator = ElectricityReadingsGenerator.new
  Hash[smart_meter_to_price_plan_accounts.keys.collect {|meter_id| 
    [meter_id, reading_generator.generate(20)]
  }]
end



 Hash[  smart_meter_to_price_plan_accounts.keys.collect {|meter_id| [meter_id, reading_generator.generate(20)] }   ]



 smart_meter_to_price_plan_accounts.keys.collect {|meter_id| [meter_id, reading_generator.generate(20)] }


smart_meter_to_price_plan_accounts.keys.collect {|meter_id| meter_id }


["smart-meter-0",[{"time"=>"2021-10-20T15:20:51-05:00", "reading"=>0.9686043876169836}]]


Hash["smart-meter-0",[{"time"=>"2021-10-20T15:20:51-05:00", "reading"=>0.9686043876169836}]]












Hash[

[["smart-meter-0",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.48226421998418},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.415052539720668}]],
 ["smart-meter-1",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.1146010452429995},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.2648167539800543}]],
 ["smart-meter-2",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.1718245947154782},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>0.5988328750351586}]],
 ["smart-meter-3",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>0.6274818428509007},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.2491530111118334}]],
 ["smart-meter-4",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.4502064259056247},
   {"time"=>"2021-10-20T15:24:50-05:00", "reading"=>0.567514961966133},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>0.7518152471043478}]]]
]



[["smart-meter-0",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.48226421998418},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.415052539720668}]],
 ["smart-meter-1",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.1146010452429995},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.2648167539800543}]],
 ["smart-meter-2",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.1718245947154782},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>0.5988328750351586}]],
 ["smart-meter-3",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>0.6274818428509007},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>1.2491530111118334}]],
 ["smart-meter-4",
  [{"time"=>"2021-10-20T15:25:08-05:00", "reading"=>1.4502064259056247},
   {"time"=>"2021-10-20T15:24:50-05:00", "reading"=>0.567514961966133},
   {"time"=>"2021-10-20T15:24:49-05:00", "reading"=>0.7518152471043478}]]]




[
  [     "aaaaa",
    [
      {
        "time"=>"2021-10-20T15:25:08-05:00",
        "reading"=>1.48226421998418
      },
     
    ]
  ],
  [
    "bbbbb",
    [
      {
        "time"=>"2021-10-20T15:25:08-05:00",
        "reading"=>1.1146010452429995
      },
     
    ]
  ],
  [
    "ccccccc",
    [
      {
        "time"=>"2021-10-20T15:25:08-05:00",
        "reading"=>1.1718245947154782
      },
    ]
  ],
  [
    "vvvvvvvvvvvv",
    [
      {
        "time"=>"2021-10-20T15:25:08-05:00",
        "reading"=>0.6274818428509007
      },
    ]
  ],
  [
    "eeeeeeeeeeee",
    [
      {
        "time"=>"2021",
        "reading"=>1.45
      },
    ]
  ]
]






Hash[[  [     "aaaaa",    [      {        "time"=>"2021-10-20T15:25:08-05:00",        "reading"=>1.48226421998418      },         ]  ],  [    "bbbbb",    [      {        "time"=>"2021-10-20T15:25:08-05:00",        "reading"=>1.1146010452429995      },         ]  ],  [    "ccccccc",    [      {        "time"=>"2021-10-20T15:25:08-05:00",        "reading"=>1.1718245947154782      },    ]  ],  [    "vvvvvvvvvvvv",    [      {        "time"=>"2021-10-20T15:25:08-05:00",        "reading"=>0.6274818428509007      },    ]  ],  [    "eeeeeeeeeeee",    [      {        "time"=>"2021",        "reading"=>1.45      },    ]  ]]]






Hash[[  [ "a",[{"time"=>"2021","reading"=>1.482}]], ["b",[{"time"=>"20212","reading"=>1.11}]] ]]



Hash[  [ [ "a",[1]], ["b",[2]]]  ]
Hash[[[1,1],[2,2]]]