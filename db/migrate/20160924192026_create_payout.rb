class CreatePayout < ActiveRecord::Migration
  def change
    create_table :payouts do |t|
      t.string :merchant_id
      t.string :account_id
      t.float :amt
      t.boolean :paid
    end
  end
end
