pub struct Player {
    pub health: u32,
    pub mana: Option<u32>,
    pub level: u32,
}

impl Player {
    pub fn revive(&self) -> Option<Player> {
        if self.health == 0 {
            let mut player = Player {
                health: 100,
                mana: None,
                level: self.level,
            };
            if self.level >= 10 {
                player.mana = Some(100);
            }
            Some(player)
        } else {
            None
        }
    }

    pub fn cast_spell(&mut self, mana_cost: u32) -> u32 {
        if self.mana.is_some() {
            let mana = self.mana.unwrap();
            if mana >= mana_cost {
                self.mana = Some(mana - mana_cost);
                2 * mana_cost
            } else {
                0
            }
        } else {
            if mana_cost >= self.health {
                self.health = 0;
            } else {
                self.health -= mana_cost;
            }
            0
        }
    }
}
