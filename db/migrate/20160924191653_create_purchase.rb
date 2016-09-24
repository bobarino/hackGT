class CreatePurchase < ActiveRecord::Migration
  def change
    create_table :purchases do |t|
      t.string :merchant_id
      t.string :account_id
      t.float :amt
      t.boolean :paid
      t.boolean :ext

    end
  end
end
